# ``WKInternalsNotes/WKContentView/formAccessoryView``

フォーム入力用のアクセサリビューを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKFormAccessoryView *formAccessoryView;
```

## Default Value
Apple TV / Vision では `nil`。それ以外は必要に応じて生成した `WKFormAccessoryView` を返す。

## Discussion
`PLATFORM(APPLETV)` と Vision UI では常に `nil`。それ以外は `inputAssistantItem` を使って `WKFormAccessoryView` を遅延生成し、保持中のインスタンスを返す。

## References
- [`WKContentViewInteraction.h#L405`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L405)
- [`WKContentViewInteraction.mm#L6297`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6297)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
