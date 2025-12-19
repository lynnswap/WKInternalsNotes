# ``WKInternalsNotes/WKContentView/dataListTextSuggestionsInputView``

datalist の候補入力ビューを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong) UIView <WKFormControl> *dataListTextSuggestionsInputView;
```

## Default Value
未設定の場合は `nil`。

## Discussion
getter は `_dataListTextSuggestionsInputView` を返す。setter は同一インスタンスの場合は何もせず、更新時に必要なら `reloadInputViews` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L537`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L537)
- [`WKContentViewInteraction.mm#L9590`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9590)
- [`WKContentViewInteraction.mm#L9600`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9600)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
