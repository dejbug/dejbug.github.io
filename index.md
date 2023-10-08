# A typical day

/// #current-nesting-level `0`. Woke up. (Went bio. Made coffee.) Turned on. Spliced in.

/// #current-nesting-level `1` #pairer. Continued investigating how long rewriting `bbpPairings` https://github.com/BieremaBoyzProgramming/bbpPairings into a WAGI https://github.com/deislabs/wagi would take. Exceptions are the problem.
https://github.com/WebAssembly/wasi-sdk#notable-limitations
https://github.com/WebAssembly/exception-handling/blob/main/proposals/exception-handling/Exceptions.md
https://emscripten.org/docs/porting/exceptions.html
https://github.com/emscripten-core/emscripten/issues/12475
**Developed the pressing need**, while browsing the source, to open include filepaths with a hotkey. That is, an editor feature is needed where moving the caret over a string and hitting a keyboard combination will (attempt to) run the string through the open command. **Stopped everyting** to write that editor plugin.

/// #current-nesting-level `2` #st-opener. Wrote the basic framework for a SublimeText https://www.sublimetext.com/docs/api_reference.html plugin. Working at the non-boilerplate logic. Get line at caret pos and the relative caret pos within it. Search both the pre-caret and post-caret text for a include path delimiter. Paths are delimited either by "" or <>. Try opening it relative to document path. Try opening it relative to current working path. Decided to write long, self-documenting function names. **Developed the pressing need** to type only the unique prefix of a word and have the editor autocomplete it. SublimeText is horrible for this.
https://forum.sublimetext.com/t/autocomplete-on-exact-matches/60549
https://github.com/sublimehq/sublime_text/issues/3434
https://github.com/sublimehq/sublime_text/issues/3280
Almost stopped everyting to write that editor plugin. **Stopped everything** to write this blog entry on it instead. That plugin would need to wait for an auto-complete trigger, then parse the document into identifiers (does ST give us access to their internal identifier buffers?), then autocomplete if unique prefix found.

/// #current-nesting-level `3` #blog-1. **Stopped everything** to change the way `blog.py` https://github.com/dejbug/dejbug.github.io/blob/master/blog.py renders **bold** text. Done.

/// #current-nesting-level `2` #st-opener. Continued writing the include filepath opener. Maybe a better way would be to have two hotkeys. One for cycling through all the possible strings that look like paths on the current line and selecting them. The other for trying to open the selection as a filepath.

/// #current-nesting-level `3` #st-autocomplete. Thinking about the exact-prefix-autocompleter again. It would be nice to extend the concept of exactness here a little. Given two functions like `extendWordToPathAtCaret` and `extendWordToPathAtPos`, one would have to type `extendWordToPathAtP` for autocomplete to be possible, completing only 2 chars out of 21. Why not exploit the camel-casing? `ewtpac` and `ewtpap`. Or maybe use globbing? `ex*Wo*Ca` and `ex*Wo*Pos`. Note how the final `*` is unnecessary, being implied by the autocompletion action. Note also how the one is a special case of the other: each capital starting a new trailing-`*`-implied globbing context: `e*W*T*P*A*C` becomes `eWTPAC`. An infix index could make it skip that many camel-cased (**cc**) word: `ex4Car` and `ex4Pos`. A suffix index could be provided to match the n-th candidate of a non-unique prefix group: `exWoPA:2`. A prefix flag could be added to switch to more elaborate matching strategies: `soundex:E235:2` (a rather contrived example). Normally one would learn, through repetitious typing, a function name's "syllable signature", to coin a term: `exwopaca` and `exwopapo`. Each syllable being shorthand for a cc-word; a `*` implied for omitted syllables.

/// #current-nesting-level `4` #blog-2. **Stopped everything** to make `blog.py` https://github.com/dejbug/dejbug.github.io/blob/master/blog.py hard-break single code lines, avoiding inline voidspace due to block justification. Done.

/// #current-nesting-level `2` #st.opener. If the caret is on a line including filepaths but not exactly within a filepath string, make it work anyway. In other words: If no filepath is found around the caret, try opening the first filepath found on the line, if any. Obviously, `#include`s are the simplest of all cases. A simple regex would do. To speed things up, we'll rename the plugin from `SuperGeneralFileOpener` to `IncludeOpener` and handle only what is possible with regex and only for the languages we're using.

/// #current-nesting-level `3` #st-opener-general. As for the more general opener, the question is: what does a filepath look like? If filepaths are the words, what is the common alphabet? Since I'm working on Linux I can't just scan for strings of valid filepath chars: all chars are valid filepath chars on Linux. But I am taking care to avoid spaces in my filepaths, which means we could simplify by considering only words (whitespace-delimited strings). A simple regex would do: finditer, then look for a match with the caret pos between start/end. Alas, the most general case can rely on no assumptions: any substring could be a filepath. Bascially, for every string `HAYSTACK = line[i:] for i in range(len(line))`, you would go through every line `NEEDLE` in `file.listing` e.g. (`find / --type f > file.listing`) and check whether `HAYSTACK.startswith(NEEDLE)`. Which is impractical. Clearly a few basic assumptions are indispensable. I will try to figure this out later.

/// #current-nesting-level `2` #st.opener. We need assumptions then. Include paths are relative to the compiler's search paths, which can be user-modified at invocation time. This means simply that we don't know. We don't where to look for the include paths. Best guess ist that the default search paths are used. Relative to the project's root, not relative to the current document. Do we start at the document root and work our way up the filesystem? So with `#include <f1/f2/n.h>`, we search the `.c` file's siblings for `f1`, then we search the parent folder, and so on. Once we find it. When we find a folder that has `f1`, we have a candidate root e.g. `/home/user/projects/project1/f1/`. So now we try: `/home/user/projects/project1/f1/f2/n.h`, if it fails, what? Continue searching up the file tree for `f1`. For a document nested `S` subfolders down the file tree, we get to call that many times into `os.path.exists`, plus the `R` times for each candidate root. That is not too bad.

/// #current-nesting-level `3`. I'm hungry. And I want to solve some chess puzzles. https://lichess.org/streak ...

/// #current-nesting-level `0`. Woke up. (Went bio. Made coffee. Called mother.) Turned on. Spliced in.

/// #current-nesting-level `2` #st.opener. Ok. Finished. Cleaned it up even. But I've noticed how I tend to interleave two function naming styles: easy to type versus easy to remember. The former is short and sweet and is an attempt to reuse the vocabulary of e.g. the Python library. The latter is long and cumbersome to type but is nicely self-documenting. Done.

/// #current-nesting-level `1` #pairer. Ok, so. Armed with the new include opener I'm going to quickly browse through the sources and find the compilation module with the smallest exceptions footprint. Let's see whether we can home in on a good-enough substitute error handling mechanism.

/// #current-nesting-level `2` #pairer. So, I've looked at some of the code and I'm thinking that the best way might be to maintain a global stack for pushing throw arguments onto. So that where it says:
```cpp
throw std::invalid_argument("");
```
we could simply turn it into:
```cpp
THROW(std::invalid_argument, "");
```
The `THROW` macro would push the args then return a dummy (arbitrary but valid) value. The computation continues as if nothing happened. Only in the main would we check whether any errors had occurred. Now, this changes the semantics of exceptions. There could be an edge case where we could enter an infinite loop. So `THROW` must check whether we've exceeded some maximum stack element count and call `abort()`. More worrying is the possibility that "arbitrary but valid" values might lead to infinite loops. So ok. This might work but again it requires grokking the code. We should probably just print the error and `abort()` when something throws. So:
```cpp
#define THROW(ex, msg) do{\
	std::cout << #ex << ": " << msg << '\n';\
	abort();\
	}while(0)
```

/// #current-nesting-level `3` #blog-highlighter. I notice that my blog's code highlighting still uses some colors that are more suitable for bright backgrounds. This time I will need to change the C++ preprocessor colors from dark blue to bright blue. I've already forgotten where GNU's `source-highlight` stores its config files. Sigh. So `pacman -Ql source-highlight`. Yikes! Ok, so `pacman -Ql source-highlight | cut -d' ' -f2 | xargs dirname | sort | uniq`. Hmm. `ll /usr/share/source-highlight`. Aha. Hmmmm. `ls -1 /usr/share/source-highlight | cut -d'.' -f2 | sort | uniq`. Ok, so:

```sh
$ for ext in `ls -1 /usr/share/source-highlight | cut -d'.' -f2 | sort | uniq`; do\
	echo -n $ext' '; ls -1 /usr/share/source-highlight/*.$ext | wc -l; done
css 46
defaults 1
lang 114
map 2
outlang 28
style 10
```

```sh
$ ls -1 /usr/share/source-highlight/*.defaults
/usr/share/source-highlight/style.defaults
$ ls -1 /usr/share/source-highlight/*.map
/usr/share/source-highlight/lang.map
/usr/share/source-highlight/outlang.map
```

```sh
$ grep cpp /usr/share/source-highlight/lang.map
moc = cpp.lang
cpp = cpp.lang
C = cpp.lang
cc = cpp.lang
cxx = cpp.lang
h = cpp.lang
hh = cpp.lang
H = cpp.lang
hpp = cpp.lang
hxx = cpp.lang
```

```sh
$ grep include /usr/share/source-highlight/cpp.lang
include "c_comment.lang"
include "c_preprocessor.lang"
include "number.lang"
include "c_string.lang"
include "symbols.lang"
include "function.lang"
include "clike_vardeclaration.lang"
```

/// #current-nesting-level `4` #blog-highlighter. I realize now that there is another way of providing custom stylesheets to `source-highlight`, via the `--outlang-def` option rather than the more obviously named `--style-file` that I've used so far. In fact, turns out you can even combine the two. Which is handy because some lexer groups are mapped to the same color! Ok so let's define a more pleasant palette against my "#333" background then.

/// #current-nesting-level `5` #blog-parser. So I've out the contents of `blog.py` inside a blog entry's code block and ran that through `render.py` so I could tweak the colors but, wouldn't you know it, inside the python code I'm using the triple backtick lexeme (that starts and ends a code block) inside a regex, obviously. So `source-higlight` complains about a language inference being impossible for that unintended second code block. So let's rewrite the regex to pickup only those backticks that start flush with the line.

/// #current-nesting-level `6` #blog-library. I've noticed that I've duplicated some code between `blog.py` and `render.py`. Forgot that I've already implemented an algo in the one when I needed it in the other. Should put generic things into a separate library.

/// #current-nesting-level `4` #blog-highlighter. Ok. Committed. Done.

/// #current-nesting-level `3` #st-opener-2. Of course I will need one more, much simpler plugin. While I'm editing a header file, a hotkey should open (or activate, if already open) the corresponding source.

/// #current-nesting-level `2` #pairer. I haven't written C++ in a long while now. Let's take this one slow.

/// #current-nesting-level `3` #break . I'm hungry. And I want to watch something. That Wheel of Time adaptation is not too bad.

/// #current-nesting-level `2` #pairer. Preliminary tests run fine. `globals.h` looks like this now.

```cpp
#ifndef GLOBALS_H
#define GLOBALS_H

#include <iostream>

#define THROW(x, m) do {\
	std::cout << #x << ": " << (m) << '\n';\
	std::cout.flush();\
	abort();\
} while(0);

#endif // GLOBALS_H
```

/// #current-nesting-level `3` #bash-1. Needed a poor man's source grepper. Done.

```sh
list-cpp-h() {
    local Dir=$1
    [[ -z $Dir ]] && Dir=.
    find $Dir \( -name '*.cpp' -or -name '*.h' \)
}

grep-cpp-h() {
    if [[ -z $1 ]]; then
        echo "usage: grep-cpp-h [root-dir] pattern"
    elif [[ -z $2 ]]; then
        list-cpp-h | xargs grep -nHE "$1"
    else
        list-cpp-h $1 | xargs grep -nHE "$2"
    fi
}
```

/// #current-nesting-level `3` #st.st-opener-2. `Ctrl+o` tries to open the include file referenced on the current line. `Ctrl+Shift+o` opens the currently active document's corresponding source file. Done.

/// #current-nesting-level `2` #pairer. One annoying thing about the `bbpPairings` code is that much of the logic is in header files, prompting the recompilation of all sources that include it. And I want to test every single throw I modify. I hate this kind of work. Good thing we decided to simply skip the generator and checker. `globals.h` looks like this now:

```cpp
#define THROW(x, m) do {\
	std::cout << __FILE__ << ':' << __LINE__ <<\
		" [" << #x << "] " << (m) << '\n';\
	std::cout.flush();\
	std::exit(-1);\
} while(0)
```

/// #current-nesting-level `3` #st.st-opener-3. Because I've remapped the open dialog hotkey with it, it needs to default to showing the open dialog if no include file could be opened. Done.

/// #current-nesting-level `2` #pairer. Whaddayaknow! There had been fewer throws to handle than expected. I haven't walked through all the catches yet to see whether some throws are recoverable. It would require a second macro that doesn't call `exit`/`terminate`/`abort`. Also it might be useful to return an exit code. That alone would require more closely looking at the catches. So something like this:

```cpp
#define WARN(x, m)    // Just print, don't terminate.
#define EXIT(x, m, c) // Terminate with error code.
#define FAIL(x, m) EXIT(x, m, EXIT_FAILURE)
```

/// #current-nesting-level `3` #pairer-wasi. Was about to build it in WASM but it gives me an error I didn't get before:

```
[wasm-validator error in function 1971] unexpected false: Bulk memory operations require bulk memory [--enable-bulk-memory], on
(memory.copy
 (local.get $0)
 (local.get $1)
 (local.get $2)
)
[wasm-validator error in function 1972] unexpected false: Bulk memory operations require bulk memory [--enable-bulk-memory], on
(memory.copy
 (local.get $0)
 (local.get $1)
 (local.get $2)
)
[wasm-validator error in function 1973] unexpected false: Bulk memory operations require bulk memory [--enable-bulk-memory], on
(memory.fill
 (local.get $0)
 (local.get $1)
 (local.get $2)
)
Fatal: error validating input
clang-16: fatal error: linker command failed with exit code 1 (use -v to see invocation)
```

https://github.com/WebAssembly/wasi-sdk/issues/254
https://github.com/llvm/llvm-project/issues/55781
https://github.com/llvm/llvm-project/issues/64909
https://github.com/wasm3/wasm3/issues/20
/ https://github.com/wasm3/wasm3/issues/20#issuecomment-1181675980

/// #current-nesting-level `4` #blog-3. The code listings with (horizontal) scrolling have strange right-padding behavior. Had to wrap them inside a div. It's messy HTML/CSS stuff. Web development is really bad for your OCD.

/// #current-nesting-level `3` #pairer-wasi. I have no idea what is going on here. It used to work in my initial tests. Let me check why my first quick hack and slash compiled and this much more careful evisceration won't. Ok, so this thread https://github.com/WebAssembly/wasi-sdk/issues/254 pointed out that it has to do with stripping the binary of meta before `wasm-opt` had a chance to do its thing. This guy https://github.com/WebAssembly/wasi-sdk/issues/254#issuecomment-1260809684 pointed out the existence of a lesser strip: instead of `--strip-all` I tried `--strip-debug` and `wasm-opt` worked fine. I had to invoke the linker separately though. Used the `-v` flag as the error message suggested. Now, how do I tell `clang` directly to do it? `-Wl,--strip-debug` doesn't hack it. `-Wl,--no-strip-all` does nothing (though it seems to be a valid flag, since there's no error either). So we need to modify the Makefile even more. For some reason I was entertaining the idea of keeping as much as possible of my rewrites external to the `bbpPairings` distribution, but why bother? A patch is "totally external", too. Ok. Got it to work. The WTF level is acceptable. Tomorrow it is going to go up into the cloudy cloud. If everything works as expected, you'd do a `curl https:/url.to -T sample.trf` and get your pairings.

! --color-title=#afe
! --color-status-1=#58cc8f
! --color-purple-haze-text=navajowhite
