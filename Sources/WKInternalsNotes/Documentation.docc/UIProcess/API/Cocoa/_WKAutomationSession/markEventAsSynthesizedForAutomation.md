# ``WKInternalsNotes/_WKAutomationSession/markEventAsSynthesizedForAutomation(_:)``

イベントを自動化由来としてマークする（macOS のみ）。

## Objective-C Declaration
```objective-c
- (void)markEventAsSynthesizedForAutomation:(NSEvent *)event;
```

## Discussion
macOS では `WebAutomationSession` にイベントを渡して、合成イベントとして記録する。

## References
- [`_WKAutomationSession.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.h#L53)
- [`_WKAutomationSession.mm#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.mm#L123)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
