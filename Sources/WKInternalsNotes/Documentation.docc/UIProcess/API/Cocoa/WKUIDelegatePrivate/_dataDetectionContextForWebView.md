# ``WKInternalsNotes/WKUIDelegatePrivate/_dataDetectionContextForWebView(_:)``

Data Detectors 用のコンテキスト辞書を返す。

## Objective-C Declaration
```objective-c
- (NSDictionary *)_dataDetectionContextForWebView:(WKWebView *)webView WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
WKContentViewInteraction で Data Detectors のコンテキストとして利用され、UIDelegate の `dataDetectionReferenceDate` では参照日付の抽出に使われる。

## References
- [`WKUIDelegatePrivate.h#L163`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L163)
- [`WKContentViewInteraction.mm#L10104`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10104)
- [`UIDelegate.mm#L1732`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1732)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
