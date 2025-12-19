# ``WKInternalsNotes/WKWebView/_promptForReplace(_:)``

`_promptForReplace` を実行する。

## Objective-C Declaration
```objective-c
- (void)_promptForReplace:(id)sender;
```

## Discussion
iOS では `WKContentViewInteraction` 側のハンドラに委譲される。

## References
- [`API/ios/WKWebViewIOS.h#L136`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L136)
- [`ios/WKContentViewInteraction.mm#L4444`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L4444)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
