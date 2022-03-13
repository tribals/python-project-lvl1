(use-modules
  (gnu packages python)
  (guix profiles))


;; TODO: define channel in order to fix deps versions
; (define my-hexlet-channel
;   (channel
;     (name 'my-hexlet)
;     (url )))

(concatenate-manifests
  (list
    (specifications->manifest
      (list
        "python@3.9"
        "poetry@1.1"))  ;; TODO: fix failing build
    (packages->manifest
      (list))))
