# ``WKInternalsNotes/_WKMediaSessionCoordinator/seekTo(_:withCompletion:)``

テスト用 coordinator では `seekTo:withCompletion:` をクライアントに転送する。

## Objective-C Declaration
```objective-c
- (void)seekTo:(double)time withCompletion:(void(^ _Nonnull)(BOOL))completionHandler;
```

## Discussion
`WKMediaSessionCoordinatorForTesting` が `seekTo` を呼び、`BOOL` 成否を `InvalidStateError` 変換に使う（`weakThis` が失われた場合も失敗扱い）。

## References
- [`WKWebViewPrivateForTesting.h#L223`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L223)
- [`WKWebViewTesting.mm#L825`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L825)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
