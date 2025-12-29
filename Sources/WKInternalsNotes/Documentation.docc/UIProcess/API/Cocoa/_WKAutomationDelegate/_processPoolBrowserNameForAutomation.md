# ``WKInternalsNotes/_WKAutomationDelegate/_processPoolBrowserNameForAutomation(_:)``

オートメーション用のブラウザ名を返す。

## Objective-C Declaration
```objective-c
- (NSString *)_processPoolBrowserNameForAutomation:(WKProcessPool *)processPool WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
`AutomationClient::browserName` から呼び出され、未実装の場合はアプリの表示名/バンドル名を使用する。

## References
- [`_WKAutomationDelegate.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationDelegate.h#L38)
- [`AutomationClient.mm#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/AutomationClient.mm#L110)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
