# ``WKInternalsNotes/_WKFocusedElementInfo/userInitiated``

ユーザー操作によるフォーカスかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isUserInitiated) BOOL userInitiated;
```

## Default Value
`initWithFocusedElementInformation` の `isUserInitiated` 引数の値。

## Discussion
初期化時に `_isUserInitiated` を設定し、その値を返す。

## References
- [`_WKFocusedElementInfo.h#L87`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFocusedElementInfo.h#L87)
- [`WKContentViewInteraction.mm#L1004`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1004)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
