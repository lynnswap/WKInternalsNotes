# ``WKInternalsNotes/_WKAutomationSession/simulatingUserInteraction``

ユーザー操作のシミュレーション中かを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isSimulatingUserInteraction) BOOL simulatingUserInteraction WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
`WebAutomationSession` の `isSimulatingUserInteraction()` を返す。

## References
- [`_WKAutomationSession.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.h#L45)
- [`_WKAutomationSession.mm#L107`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.mm#L107)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
