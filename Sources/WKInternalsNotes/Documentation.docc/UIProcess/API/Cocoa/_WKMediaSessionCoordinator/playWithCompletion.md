# ``WKInternalsNotes/_WKMediaSessionCoordinator/playWithCompletion(_:)``

テスト用 coordinator では `playWithCompletion:` をクライアントに転送する。

## Objective-C Declaration
```objective-c
- (void)playWithCompletion:(void(^ _Nonnull)(BOOL))completionHandler;
```

## Discussion
`WKMediaSessionCoordinatorForTesting` が `playWithCompletion:` を呼び、`BOOL` 成否を `InvalidStateError` 変換に使う（`weakThis` が失われた場合も失敗扱い）。

## References
- [`WKWebViewPrivateForTesting.h#L224`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L224)
- [`WKWebViewTesting.mm#L837`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L837)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
