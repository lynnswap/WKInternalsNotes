# ``WKInternalsNotes/_WKActivatedElementInfo/isAnimatedImage``

アニメーション画像かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL isAnimatedImage WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Default Value
初期化時に渡された `isAnimatedImage` の値。

## Discussion
初期化時に `_animatedImage` を設定し、getter で返す。

## References
- [`_WKActivatedElementInfo.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.h#L50)
- [`_WKActivatedElementInfo.mm#L199`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L199)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
