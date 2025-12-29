# ``WKInternalsNotes/WKFullScreenViewControllerDelegate/hideUI()``

フルスクリーン UI を隠すよう通知する。

## Objective-C Declaration
```objective-c
- (void)hideUI;
```

## Discussion
`WKFullScreenWindowControllerIOS` の実装では、visionOS で QuickLook 使用時を除き `UIWindowScene` の chrome オプションを非表示にする。

## References
- [`WKFullScreenViewController.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenViewController.h#L39)
- [`WKFullScreenWindowControllerIOS.mm#L2232`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L2232)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
