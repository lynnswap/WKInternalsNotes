# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:unavailablePlugInButtonClickedWithReason:plugInInfo:)``

利用不可プラグインのボタン押下を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView unavailablePlugInButtonClickedWithReason:(_WKPlugInUnavailabilityReason)reason plugInInfo:(NSDictionary *)plugInInfo;
```

## Discussion
現行の UIProcess 実装では呼び出し箇所が見当たらず、宣言のみが存在する。

## References
- [`WKUIDelegatePrivate.h#L321`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L321)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
