# ``WKInternalsNotes/WKFullScreenViewController/hideCustomControls(_:)``

カスタムコントロールを非表示にする。

## Objective-C Declaration
```objective-c
- (void)hideCustomControls:(BOOL)hidden;
```

## Discussion
`ENABLE(VIDEO_USES_ELEMENT_FULLSCREEN)` のときのみ動作し、`_shouldHideCustomControls` を更新して `videoControlsManagerDidChange` を呼び直す。

## References
- [`WKFullScreenViewController.mm#L584`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L584)
- [`WKFullScreenViewController.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L68)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
