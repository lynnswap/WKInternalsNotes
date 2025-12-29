# ``WKInternalsNotes/WKTextFinderClient/didFindStringMatchesWithRects(_:didWrapAround:)``

検索結果の矩形とラップ有無を通知する。

## Objective-C Declaration
```objective-c
- (void)didFindStringMatchesWithRects:(const Vector<Vector<WebCore::IntRect>>&)rects didWrapAround:(BOOL)didWrapAround;
```

## Discussion
コールバック待ちがなければ何もしない。`WKTextFinderMatch` を生成し、`_usePlatformFindUI` が有効なら矩形配列を渡し、無効なら空配列で作成して先頭のコールバックに返す。

## References
- [`WKTextFinderClient.mm#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextFinderClient.mm#L54)
- [`WKTextFinderClient.mm#L290`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextFinderClient.mm#L290)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
