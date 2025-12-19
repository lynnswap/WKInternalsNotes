# ``WKInternalsNotes/WKContentView/deferringGestures``

デファリング中のジェスチャ認識器一覧を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSArray<WKDeferringGestureRecognizer *> *deferringGestures;
```

## Default Value
タッチ開始/終了のデファリング群と、必要に応じてタッチ移動・画像解析のデファリング認識器を含む。

## Discussion
各種デファリング用の `WKDeferringGestureRecognizer` を集約して返す。

## References
- [`WKContentViewInteraction.h#L735`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L735)
- [`WKContentViewInteraction.mm#L2476`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2476)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
