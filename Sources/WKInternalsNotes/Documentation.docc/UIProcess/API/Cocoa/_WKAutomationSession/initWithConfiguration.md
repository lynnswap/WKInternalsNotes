# ``WKInternalsNotes/_WKAutomationSession/initWithConfiguration(_:)``

指定した構成で自動化セッションを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithConfiguration:(_WKAutomationSessionConfiguration *)configuration NS_DESIGNATED_INITIALIZER;
```

## Discussion
`WebAutomationSession` を wrapper として構築し、渡された構成をコピーして保持する。`-init` はこの initializer を新規構成で呼び出す。

## References
- [`_WKAutomationSession.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.h#L47)
- [`_WKAutomationSession.mm#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.mm#L43)
- [`_WKAutomationSession.mm#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.mm#L48)
- [`_WKAutomationSession.mm#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.mm#L53)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
