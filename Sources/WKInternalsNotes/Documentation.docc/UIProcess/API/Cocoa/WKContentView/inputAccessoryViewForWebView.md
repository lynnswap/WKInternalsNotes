# ``WKInternalsNotes/WKContentView/inputAccessoryViewForWebView``

WebView に表示する inputAccessoryView を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UIView *inputAccessoryViewForWebView;
```

## Default Value
アクセサリが不要なら `nil`、必要ならカスタムビューまたは `formAccessoryView` を返す。

## Discussion
`requiresAccessoryView` が `NO` の場合は `nil`。それ以外は `_formInputSession` の `customInputAccessoryView` を優先し、無ければ `formAccessoryView` を返す。

## References
- [`WKContentViewInteraction.h#L730`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L730)
- [`WKContentViewInteraction.mm#L4260`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L4260)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
