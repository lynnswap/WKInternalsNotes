# ``WKInternalsNotes/WKScrollView/_contentInsetAdjustmentBehaviorWasExternallyOverridden``

外部から `contentInsetAdjustmentBehavior` が変更されたかを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic, assign, readonly) BOOL _contentInsetAdjustmentBehaviorWasExternallyOverridden;
```

## Default Value
初期化時の `contentInsetAdjustmentBehavior` が `UIScrollViewContentInsetAdjustmentAutomatic` 以外なら `YES`。

## Discussion
`setContentInsetAdjustmentBehavior:` が呼ばれると `YES` になり、`_resetContentInsetAdjustmentBehavior` で `NO` に戻る。

## References
- [`WKScrollView.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.h#L52)
- [`WKScrollView.mm#L342`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKScrollView.mm#L342)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
