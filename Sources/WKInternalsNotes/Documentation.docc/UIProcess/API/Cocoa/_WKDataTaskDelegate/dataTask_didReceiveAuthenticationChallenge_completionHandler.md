# ``WKInternalsNotes/_WKDataTaskDelegate/dataTask(_:didReceiveAuthenticationChallenge:completionHandler:)``

認証チャレンジを delegate で処理する。

## Objective-C Declaration
```objective-c
- (void)dataTask:(_WKDataTask *)dataTask didReceiveAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge completionHandler:(void (^)(NSURLSessionAuthChallengeDisposition, NSURLCredential * _Nullable))completionHandler;
```

## Discussion
delegate が未実装の場合は `RejectProtectionSpaceAndContinue` を選択する。実装されている場合は `NSURLSessionAuthChallengeDisposition` を `AuthenticationChallengeDisposition` に変換して完了させる。

## References
- [`_WKDataTaskDelegate.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTaskDelegate.h#L49)
- [`_WKDataTask.mm#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L61)
- [`_WKDataTask.mm#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L67)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
