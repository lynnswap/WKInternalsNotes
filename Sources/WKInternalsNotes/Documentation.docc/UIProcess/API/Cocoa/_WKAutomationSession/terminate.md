# ``WKInternalsNotes/_WKAutomationSession/terminate()``

自動化セッションを終了する。

## Objective-C Declaration
```objective-c
- (void)terminate WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
`WebAutomationSession::terminate()` を呼び出して終了処理を開始する。

## References
- [`_WKAutomationSession.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.h#L49)
- [`_WKAutomationSession.mm#L112`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.mm#L112)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
