# ``WKInternalsNotes/WKSOAuthorizationDelegate/setSession(_:)``

SOAuthorizationSession を設定する。

## Objective-C Declaration
```objective-c
- (void)setSession:(RefPtr<WebKit::SOAuthorizationSession>&&)session;
```

## Discussion
メインスレッドを要求し、`_session` にコピーして保持する。`session` が非nullの場合は `shouldStart()` を呼ぶ。

## References
- [`WKSOAuthorizationDelegate.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/SOAuthorization/WKSOAuthorizationDelegate.h#L36)
- [`WKSOAuthorizationDelegate.mm#L153`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/SOAuthorization/WKSOAuthorizationDelegate.mm#L153)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
