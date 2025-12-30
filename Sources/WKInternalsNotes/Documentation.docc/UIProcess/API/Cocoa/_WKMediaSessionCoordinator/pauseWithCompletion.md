# ``WKInternalsNotes/_WKMediaSessionCoordinator/pauseWithCompletion(_:)``

テスト用 coordinator では `pauseWithCompletion:` をクライアントに転送する。

## Objective-C Declaration
```objective-c
- (void)pauseWithCompletion:(void(^ _Nonnull)(BOOL))completionHandler;
```

## Discussion
`WKMediaSessionCoordinatorForTesting` が `pauseWithCompletion:` を呼び、`BOOL` 成否を `InvalidStateError` 変換に使う（`weakThis` が失われた場合も失敗扱い）。

## References
- [`WKWebViewPrivateForTesting.h#L225`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L225)
- [`WKWebViewTesting.mm#L849`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L849)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
