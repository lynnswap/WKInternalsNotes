# ``WKInternalsNotes/WKFullScreenViewController/resetSupportedOrientations()``

フルスクリーン時のサポート回転設定を解除する。

## Objective-C Declaration
```objective-c
- (void)resetSupportedOrientations;
```

## Discussion
`_supportedOrientations` を `std::nullopt` に戻し、`setNeedsUpdateOfSupportedInterfaceOrientations` を呼ぶ。

## References
- [`WKFullScreenViewController.mm#L280`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.mm#L280)
- [`WKFullScreenViewController.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L66)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
