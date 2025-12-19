# ``WKInternalsNotes/WKScrollView/_wk_leftEdgeEffect()``

左エッジの `WKUIScrollEdgeEffect` を返す。

## Objective-C Declaration
```objective-c
- (WKUIScrollEdgeEffect *)_wk_leftEdgeEffect;
```

## Default Value
元の `leftEdgeEffect` が存在しない場合は `nil`。

## Discussion
既存の `UIScrollEdgeEffect` を取得し、未ラップなら `WKUIScrollEdgeEffect` を生成してキャッシュする。

## References
- [`WKScrollView.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L62)
- [`WKScrollView.mm#L623`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L623)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
