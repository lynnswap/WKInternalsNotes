# ``WKInternalsNotes/_WKAutomationSession/paired``

自動化セッションがペアリング済みかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isPaired) BOOL paired;
```

## Discussion
`WebAutomationSession` の `isPaired()` をそのまま返す。

## References
- [`_WKAutomationSession.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.h#L42)
- [`_WKAutomationSession.mm#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.mm#L97)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
