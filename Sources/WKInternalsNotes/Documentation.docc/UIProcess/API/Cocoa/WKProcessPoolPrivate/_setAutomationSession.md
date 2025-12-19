# ``WKInternalsNotes/WKProcessPool/_setAutomationSession(_:)``

Automation セッションを設定する。

## Objective-C Declaration
```objective-c
- (void)_setAutomationSession:(_WKAutomationSession *)automationSession WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
`_automationSession` を更新し、`setAutomationSession` にセッション（または nullptr）を渡す。

## References
- [`WKProcessPoolPrivate.h#L113`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L113)
- [`WKProcessPool.mm#L348`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L348)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
