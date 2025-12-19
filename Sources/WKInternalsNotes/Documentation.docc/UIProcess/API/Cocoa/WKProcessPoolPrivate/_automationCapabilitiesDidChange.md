# ``WKInternalsNotes/WKProcessPool/_automationCapabilitiesDidChange()``

Automation の能力変更をプロセスプールへ通知する。

## Objective-C Declaration
```objective-c
- (void)_automationCapabilitiesDidChange WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
`updateAutomationCapabilities()` を呼び出す。

## References
- [`WKProcessPoolPrivate.h#L112`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L112)
- [`WKProcessPool.mm#L343`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L343)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
