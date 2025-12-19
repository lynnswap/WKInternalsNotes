# ``WKInternalsNotes/_WKAutomationSession/pendingTermination``

終了待ち状態かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isPendingTermination) BOOL pendingTermination WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`WebAutomationSession` の `isPendingTermination()` を返す。

## References
- [`_WKAutomationSession.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.h#L43)
- [`_WKAutomationSession.mm#L102`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.mm#L102)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
