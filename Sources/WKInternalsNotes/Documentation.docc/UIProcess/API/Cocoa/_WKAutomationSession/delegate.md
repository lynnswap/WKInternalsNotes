# ``WKInternalsNotes/_WKAutomationSession/delegate``

自動化セッションの delegate を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id <_WKAutomationSessionDelegate> delegate;
```

## Default Value
`initWithConfiguration:` では delegate を設定しないため `nil`。

## Discussion
setter は `WeakObjCPtr` に保持し、`WebAutomationSession` の client を `AutomationSessionClient` に差し替える。`nil` を渡すと client を解除する。

## References
- [`_WKAutomationSession.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.h#L41)
- [`_WKAutomationSession.mm#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.mm#L48)
- [`_WKAutomationSession.mm#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.mm#L71)
- [`_WKAutomationSession.mm#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.mm#L76)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
