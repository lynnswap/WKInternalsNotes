# ``WKInternalsNotes/_WKAutomationSession/wasEventSynthesizedForAutomation(_:)``

イベントが自動化で合成されたかどうかを返す（macOS のみ）。

## Objective-C Declaration
```objective-c
- (BOOL)wasEventSynthesizedForAutomation:(NSEvent *)event;
```

## Discussion
macOS では `WebAutomationSession` の判定結果をそのまま返す。

## References
- [`_WKAutomationSession.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.h#L52)
- [`_WKAutomationSession.mm#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.mm#L117)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
