# ``WKInternalsNotes/_WKAutomationSession/sessionIdentifier``

自動化セッションの識別子を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSString *sessionIdentifier;
```

## Default Value
`WebAutomationSession` は初期値として `"Untitled Session"` を使う。

## Discussion
getter は `_session->sessionIdentifier()` を `NSString` に変換して返し、setter は `WebAutomationSession` に値を渡す。

## References
- [`_WKAutomationSession.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.h#L38)
- [`_WKAutomationSession.mm#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.mm#L82)
- [`_WKAutomationSession.mm#L87`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.mm#L87)
- [`WebAutomationSession.h#L372`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Automation/WebAutomationSession.h#L372)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
