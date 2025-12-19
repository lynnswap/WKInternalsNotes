# ``WKInternalsNotes/WKScrollView/_wk_rightEdgeEffect()``

右エッジの `WKUIScrollEdgeEffect` を返す。

## Objective-C Declaration
```objective-c
- (WKUIScrollEdgeEffect *)_wk_rightEdgeEffect;
```

## Default Value
元の `rightEdgeEffect` が存在しない場合は `nil`。

## Discussion
既存の `UIScrollEdgeEffect` を取得し、未ラップなら `WKUIScrollEdgeEffect` を生成してキャッシュする。

## References
- [`WKScrollView.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L63)
- [`WKScrollView.mm#L637`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L637)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
