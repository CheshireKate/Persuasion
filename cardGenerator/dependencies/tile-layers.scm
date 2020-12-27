; tile-layers.scm
; by Saul Goode and Rob Antonishen
; http://ffaat.pointclark.net

; Version 1.0 (20100430)

; Description
;
; This script will tile layers so that each layer is centered
; in a non-overlapping panel in a manner that all layers are visible.
; It allows specifying the width, height, or will best fit to a square.
; There are options for spacing the images out and drawing a grid.
;
; This started as Saul Goode's mosaicize script 
; http://flashingtwelve.brickfilms.com/GIMP/Scripts/mosaicize.scm

; License:
;
; This program is free software; you can redistribute it and/or modify
; it under the terms of the GNU General Public License as published by
; the Free Software Foundation; either version 2 of the License, or
; (at your option) any later version. 
;
; This program is distributed in the hope that it will be useful,
; but WITHOUT ANY WARRANTY; without even the implied warranty of
; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
; GNU General Public License for more details.
;
; The GNU Public License is available at
; http://www.gnu.org/copyleft/gpl.html

(define (script-fu-tile-layers image drawable mode size spacing drawgrid-flag gridcolour)
  (let* (
    (layers  (vector->list (cadr (gimp-image-get-layers image))))
    (max-bounds 0)
    (num-cols (cond 
                ((= mode 0) (trunc (+ (sqrt (length layers)) 0.99999))) ; Square
                ((= mode 1) (min size (length layers))); Specify Across
                ((= mode 2) (trunc (+ (/ (length layers) (min (length layers) size) 0.99999)))))) ; Specify Down
    (num-rows (cond
                ((or (= mode 0) (= mode 1)) (trunc (+ (/ (length layers) num-cols) 0.99999)))
                ((= mode 2) (min (length layers) size))))
    (window 0)
    (grid 0)
    (row 0)
    (col 0)
   )

  (gimp-context-push)
  (gimp-image-undo-group-start image)
  (set! max-bounds
    (let loop ((layer layers)
               (max-width 0)
               (max-height 0))
               (if (null? layer)
                 (list max-width max-height)
                 (loop (cdr layer)
                       (max max-width (car (gimp-drawable-width (car layer))))
                       (max max-height (car (gimp-drawable-height (car layer))))
                       ))))
  (set! window (car (gimp-layer-new image
                                    (+ (* num-cols (car max-bounds)) (* num-cols spacing) spacing)
                                    (+ (* num-rows (cadr max-bounds)) (* num-rows spacing) spacing)
                                    (+ 1 (* (car (gimp-image-base-type image)) 2))
                                   "Frames"
                                    100
                                    NORMAL-MODE)))
  (gimp-image-add-layer image window -1)
  (gimp-image-lower-layer-to-bottom image window)
  (gimp-image-resize-to-layers image)
  (gimp-layer-set-offsets window 0 0)
  (gimp-drawable-fill window BACKGROUND-FILL)
  (let loop ((layer (reverse layers))
             (row 0)
             (col 0))
             (if (pair? layer)
               (begin
                 (let* (
                     (x (+ (* col (+ (car max-bounds) spacing)) spacing))
                     (y (+ (* row (+ (cadr max-bounds) spacing)) spacing))
                     )
                   (gimp-layer-set-offsets (car layer)
                                       (+ x (/ (- (car  max-bounds) 
                                                  (car (gimp-drawable-width  (car layer))))
                                                2))
                                       (+ y (/ (- (cadr max-bounds) 
                                                  (car (gimp-drawable-height (car layer))))
                                                2)))
                   (set! col (+ col 1))
                   (if (= col num-cols)
                     (begin
                       (set! col 0)
                       (set! row (+ row 1))
                       )
                     )
                   (loop (cdr layer)
                         row
                         col)))))
  (when (and (equal? drawgrid-flag TRUE) (> spacing 0))
    (set! grid (car (gimp-layer-new image
                                    (+ (* num-cols (car max-bounds)) (* num-cols spacing) spacing)
                                    (+ (* num-rows (cadr max-bounds)) (* num-rows spacing) spacing)
                                    (+ 1 (* (car (gimp-image-base-type image)) 2))
                                   "Grid"
                                    100
                                    NORMAL-MODE)))
    (gimp-image-add-layer image grid 0)
    (gimp-image-raise-layer-to-top image grid)
    (plug-in-grid RUN-NONINTERACTIVE image grid spacing (+ (car max-bounds) spacing) (trunc (/ spacing 2)) gridcolour 255
                                                spacing (+ (cadr max-bounds) spacing) (trunc (/ spacing 2)) gridcolour 255
                                                0 0 0 gridcolour 0))
  (gimp-image-undo-group-end image)
  (gimp-context-pop)
  (gimp-displays-flush)
  )
)

(script-fu-register "script-fu-tile-layers"
  "Tile Layers..."
  "Translate layers into a grid."
  "Saul Goode and Rob Antonishen"
  "Saul Goode and Rob Antonishen"
  "April 2010"
  "*"
  SF-IMAGE      "Image"    0
  SF-DRAWABLE   "Drawable" 0
  SF-OPTION     "Mode" '("Best Fit to Square" "Specify Across" "Specify Down")
  SF-ADJUSTMENT "Number of grid cells" '(2 1 100 1 5 0 0)
  SF-ADJUSTMENT "Spacing between cells" '(0 0 25 1 5 0 0)
  SF-TOGGLE     "Draw Grid" FALSE 
  SF-COLOR      "Grid Colour" (car (gimp-context-get-foreground))
)
  
(script-fu-menu-register "script-fu-tile-layers"
  "<Image>/Filters/Map"
)
