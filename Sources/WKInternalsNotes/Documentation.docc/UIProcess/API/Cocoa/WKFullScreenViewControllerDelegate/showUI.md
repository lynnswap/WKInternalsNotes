# ``WKInternalsNotes/WKFullScreenViewControllerDelegate/showUI()``

フルスクリーン UI を表示するよう通知する。

## Objective-C Declaration
```objective-c
- (void)showUI;
```

## Discussion
`WKFullScreenWindowControllerIOS` の実装では、visionOS で QuickLook 使用時を除き `UIWindowScene` の chrome オプションを復元する。

## References
- [`WKFullScreenViewController.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L38)
- [`WKFullScreenWindowControllerIOS.mm#L2218`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L2218)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
