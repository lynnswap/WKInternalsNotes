# ``WKInternalsNotes/WKContentView/singleTapGestureRecognizer``

シングルタップ判定に使う合成タップジェスチャ認識器を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UITapGestureRecognizer *singleTapGestureRecognizer;
```

## Default Value
`setUpInteraction` で生成した `WKSyntheticTapGestureRecognizer` を返す。

## Discussion
`setUpInteraction` で `WKSyntheticTapGestureRecognizer` を生成し、`_touchEventGestureRecognizer` を関連付けて `self` に追加する。getter は `_singleTapGestureRecognizer` を返す。

## References
- [`WKContentViewInteraction.h#L353`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L353)
- [`WKContentViewInteraction.mm#L1388`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1388)
- [`WKContentViewInteraction.mm#L14665`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14665)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
