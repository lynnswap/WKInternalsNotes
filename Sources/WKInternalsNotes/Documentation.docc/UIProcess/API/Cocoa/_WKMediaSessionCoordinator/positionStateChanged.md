# ``WKInternalsNotes/_WKMediaSessionCoordinator/positionStateChanged(_:)``

位置情報の更新をクライアントに伝える。

## Objective-C Declaration
```objective-c
- (void)positionStateChanged:(struct _WKMediaPositionState * _Nullable)state;
```

## Discussion
`WKMediaSessionCoordinatorForTesting` は `state` が `nullopt` の場合 `nil` を渡し、値がある場合は `_WKMediaPositionState` を組み立てて `positionStateChanged:` に渡す。

## References
- [`WKWebViewPrivateForTesting.h#L227`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L227)
- [`WKWebViewTesting.mm#L873`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L873)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
