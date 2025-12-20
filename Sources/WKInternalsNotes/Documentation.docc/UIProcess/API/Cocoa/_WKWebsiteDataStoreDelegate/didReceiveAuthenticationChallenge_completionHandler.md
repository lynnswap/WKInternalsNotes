# ``WKInternalsNotes/_WKWebsiteDataStoreDelegate/didReceiveAuthenticationChallenge(_:completionHandler:)``

認証チャレンジの処理を delegate に委譲する。

## Objective-C Declaration
```objective-c
- (void)didReceiveAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge completionHandler:(void (^)(NSURLSessionAuthChallengeDisposition disposition, NSURLCredential *credential))completionHandler;
```

## Discussion
delegate が未設定または未実装の場合は `PerformDefaultHandling` で完了する。実装済みの場合は `CompletionHandlerCallChecker` で多重呼び出しを防ぎ、`disposition` を `WebKit::AuthenticationChallengeDisposition` に変換し、`credential` を `WebCore::Credential` にして完了させる。

## References
- [`_WKWebsiteDataStoreDelegate.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreDelegate.h#L62)
- [`WKWebsiteDataStore.mm#L160`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L160)
- [`WKWebsiteDataStore.mm#L173`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L173)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
