# ``WKInternalsNotes/WKFullScreenViewController/setSupportedOrientations(_:)``

フルスクリーン時のサポート回転を設定する。

## Objective-C Declaration
```objective-c
- (void)setSupportedOrientations:(UIInterfaceOrientationMask)supportedOrientations;
```

## Discussion
`_supportedOrientations` を設定し、`setNeedsUpdateOfSupportedInterfaceOrientations` を呼ぶ。

## References
- [`WKFullScreenViewController.mm#L274`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L274)
- [`WKFullScreenViewController.h#L65`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L65)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
