# ``WKInternalsNotes/WKScrollView/_wk_bottomEdgeEffect()``

下エッジの `WKUIScrollEdgeEffect` を返す。

## Objective-C Declaration
```objective-c
- (WKUIScrollEdgeEffect *)_wk_bottomEdgeEffect;
```

## Default Value
元の `bottomEdgeEffect` が存在しない場合は `nil`。

## Discussion
既存の `UIScrollEdgeEffect` を取得し、未ラップなら `WKUIScrollEdgeEffect` を生成してキャッシュする。

## References
- [`WKScrollView.h#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L64)
- [`WKScrollView.mm#L651`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L651)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
