# ``WKInternalsNotes/_WKMediaSessionCoordinator/setTrack(_:withCompletion:)``

テスト用 coordinator では `setTrack:withCompletion:` をクライアントに転送する。

## Objective-C Declaration
```objective-c
- (void)setTrack:(NSString *_Nonnull)trackIdentifier withCompletion:(void(^ _Nonnull)(BOOL))completionHandler;
```

## Discussion
`WKMediaSessionCoordinatorForTesting` が `setTrack:withCompletion:` を呼び、`BOOL` 成否を `InvalidStateError` 変換に使う（`weakThis` が失われた場合も失敗扱い）。

## References
- [`WKWebViewPrivateForTesting.h#L226`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L226)
- [`WKWebViewTesting.mm#L861`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L861)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
