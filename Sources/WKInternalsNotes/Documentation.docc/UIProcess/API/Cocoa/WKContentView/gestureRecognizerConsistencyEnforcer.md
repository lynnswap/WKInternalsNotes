# ``WKInternalsNotes/WKContentView/gestureRecognizerConsistencyEnforcer``

ジェスチャ認識器の整合性管理用オブジェクトを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WebKit::GestureRecognizerConsistencyEnforcer& gestureRecognizerConsistencyEnforcer;
```

## Default Value
初回アクセス時に `GestureRecognizerConsistencyEnforcer` を生成し、その参照を返す。

## Discussion
未生成の場合は `lazyInitialize` で `GestureRecognizerConsistencyEnforcer` を生成し、以降は保持中の参照を返す。

## References
- [`WKContentViewInteraction.h#L346`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L346)
- [`WKContentViewInteraction.mm#L2468`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2468)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
