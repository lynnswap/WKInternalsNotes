# ``WKInternalsNotes/WKWebView/_accessibilityDidGetSpeakSelectionContent(_:)``

`_accessibilityDidGetSpeakSelectionContent` を実行する。

## Objective-C Declaration
```objective-c
- (void)_accessibilityDidGetSpeakSelectionContent:(NSString *)content WK_API_AVAILABLE(ios(11.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L782`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L782)
- [`API/ios/WKWebViewIOS.mm#L5035`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L5035)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
