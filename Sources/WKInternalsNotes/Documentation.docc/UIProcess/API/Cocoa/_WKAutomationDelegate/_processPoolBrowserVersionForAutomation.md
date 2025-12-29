# ``WKInternalsNotes/_WKAutomationDelegate/_processPoolBrowserVersionForAutomation(_:)``

オートメーション用のブラウザバージョンを返す。

## Objective-C Declaration
```objective-c
- (NSString *)_processPoolBrowserVersionForAutomation:(WKProcessPool *)processPool WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
`AutomationClient::browserVersion` から呼び出され、未実装の場合はアプリのショートバージョン文字列を使用する。

## References
- [`_WKAutomationDelegate.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationDelegate.h#L39)
- [`AutomationClient.mm#L122`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationClient.mm#L122)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
