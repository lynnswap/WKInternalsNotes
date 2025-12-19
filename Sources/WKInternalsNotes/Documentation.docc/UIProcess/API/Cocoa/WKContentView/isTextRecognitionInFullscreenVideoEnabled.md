# ``WKInternalsNotes/WKContentView/isTextRecognitionInFullscreenVideoEnabled``

フルスクリーン動画のテキスト認識が有効かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL isTextRecognitionInFullscreenVideoEnabled;
```

## Default Value
`ENABLE(IMAGE_ANALYSIS_ENHANCEMENTS)` 有効時は `preferences().textRecognitionInVideosEnabled()`、無効時は `NO`。

## Discussion
ビルドフラグに応じて、`WebPageProxy` の `textRecognitionInVideosEnabled` 設定を返す。

## References
- [`WKContentViewInteraction.h#L995`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L995)
- [`WKContentViewInteraction.mm#L13401`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L13401)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
