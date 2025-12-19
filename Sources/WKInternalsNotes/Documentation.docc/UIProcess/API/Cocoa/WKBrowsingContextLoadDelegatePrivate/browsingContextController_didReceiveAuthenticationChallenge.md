# ``WKInternalsNotes/WKBrowsingContextLoadDelegatePrivate/browsingContextController(_:didReceiveAuthenticationChallenge:)``

認証チャレンジ受信時に呼ばれる delegate フック。

## Objective-C Declaration
```objective-c
- (void)browsingContextController:(WKBrowsingContextController *)sender didReceiveAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge;
```

## Discussion
`WKBrowsingContextLoadDelegatePrivate` の optional メソッドとして定義され、`NSURLAuthenticationChallenge` を受け取ってハンドリングできる。

## References
- [`WKBrowsingContextLoadDelegatePrivate.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKBrowsingContextLoadDelegatePrivate.h#L33)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
