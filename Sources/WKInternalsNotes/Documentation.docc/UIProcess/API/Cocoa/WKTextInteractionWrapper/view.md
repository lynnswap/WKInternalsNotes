# ``WKInternalsNotes/WKTextInteractionWrapper/view``

関連する `WKContentView` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, weak) WKContentView *view;
```

## Default Value
`initWithView:` で設定され、それ以外は `nil`。

## Discussion
内部の `_view` をそのまま返す。

## References
- [`WKTextInteractionWrapper.mm#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L43)
- [`WKTextInteractionWrapper.mm#L332`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L332)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
