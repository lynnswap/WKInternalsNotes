# ``WKInternalsNotes/WKScrollView/_wk_topEdgeEffect()``

トップエッジの `WKUIScrollEdgeEffect` を返す。

## Objective-C Declaration
```objective-c
- (WKUIScrollEdgeEffect *)_wk_topEdgeEffect;
```

## Default Value
元の `topEdgeEffect` が存在しない場合は `nil`。

## Discussion
既存の `UIScrollEdgeEffect` を取得し、未ラップなら `WKUIScrollEdgeEffect` を生成してキャッシュする。

## References
- [`WKScrollView.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L61)
- [`WKScrollView.mm#L609`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L609)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
