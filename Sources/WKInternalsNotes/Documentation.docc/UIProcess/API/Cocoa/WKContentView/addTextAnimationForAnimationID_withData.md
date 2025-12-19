# ``WKInternalsNotes/WKContentView/addTextAnimationForAnimationID(_:withData:)``

テキストアニメーションを登録する。

## Objective-C Declaration
```objective-c
- (void)addTextAnimationForAnimationID:(NSUUID *)uuid withData:(const WebCore::TextAnimationData&)data;
```

## Discussion
設定が無効なら何もしない。`Final` スタイルの場合は source/destination の対応を記録し、`WKTextAnimationManager` を遅延生成してアニメーションを登録する。

## References
- [`WKContentViewInteraction.h#L935`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L935)
- [`WKContentViewInteraction.mm#L14161`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14161)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
