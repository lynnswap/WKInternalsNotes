# ``WKInternalsNotes/_WKMediaSessionCoordinator/joinWithCompletion(_:)``

テスト用 coordinator では `join` 要求をクライアントへ転送する。

## Objective-C Declaration
```objective-c
- (void)joinWithCompletion:(void(^ _Nonnull)(BOOL))completionHandler;
```

## Discussion
`WKMediaSessionCoordinatorForTesting` が `joinWithCompletion` を呼び、`BOOL` 成否を `InvalidStateError` 変換に使う（`weakThis` が失われた場合も失敗扱い）。

## References
- [`WKWebViewPrivateForTesting.h#L221`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L221)
- [`WKWebViewTesting.mm#L808`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L808)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
