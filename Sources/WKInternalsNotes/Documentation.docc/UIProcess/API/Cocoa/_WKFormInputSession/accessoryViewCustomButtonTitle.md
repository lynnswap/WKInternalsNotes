# ``WKInternalsNotes/_WKFormInputSession/accessoryViewCustomButtonTitle``

アクセサリビューのカスタムボタンのタイトル。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSString *accessoryViewCustomButtonTitle;
```

## Default Value
`nil`。

## Discussion
getter は `formAccessoryView` の `autoFillButtonItem.title` を返す。setter ではタイトルが空でなければボタンを表示してタイトルを設定し、空ならボタンを非表示にする。小画面端末でなければ `reloadInputViews` を呼ぶ。

## References
- [`WKContentViewInteraction.mm#L802`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L802)
- [`WKContentViewInteraction.mm#L807`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L807)
- [`_WKFormInputSession.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFormInputSession.h#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
